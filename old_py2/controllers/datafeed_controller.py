import logging
import os
import datetime
import tba_config
import time
import json

from google.appengine.api import taskqueue
from google.appengine.ext import ndb
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from consts.event_type import EventType
from consts.media_type import MediaType
from consts.media_tag import MediaTag

from datafeeds.datafeed_fms_api import DatafeedFMSAPI
from datafeeds.datafeed_tba import DatafeedTba
from datafeeds.datafeed_resource_library import DatafeedResourceLibrary
from helpers.district_manipulator import DistrictManipulator
from helpers.event_helper import EventHelper
from helpers.event_manipulator import EventManipulator
from helpers.event_details_manipulator import EventDetailsManipulator
from helpers.event_team_manipulator import EventTeamManipulator
from helpers.match_manipulator import MatchManipulator
from helpers.match_helper import MatchHelper
from helpers.award_manipulator import AwardManipulator
from helpers.media_manipulator import MediaManipulator
from helpers.team_manipulator import TeamManipulator
from helpers.district_team_manipulator import DistrictTeamManipulator
from helpers.robot_manipulator import RobotManipulator
from helpers.event.offseason_event_helper import OffseasonEventHelper
from helpers.suggestions.suggestion_creator import SuggestionCreator

from models.district_team import DistrictTeam
from models.event import Event
from models.event_details import EventDetails
from models.event_team import EventTeam
from models.media import Media
from models.robot import Robot
from models.sitevar import Sitevar
from models.team import Team

from sitevars.website_blacklist import WebsiteBlacklist


class FMSAPIEventAlliancesEnqueue(webapp.RequestHandler):
    """
    Handles enqueing getting alliances
    """
    def get(self, when):
        if when == "now":
            events = EventHelper.getEventsWithinADay()
            events = filter(lambda e: e.official, events)
        elif when == "last_day_only":
            events = EventHelper.getEventsWithinADay()
            events = filter(lambda e: e.official and e.ends_today, events)
        else:
            event_keys = Event.query(Event.official == True).filter(Event.year == int(when)).fetch(500, keys_only=True)
            events = ndb.get_multi(event_keys)

        for event in events:
            taskqueue.add(
                queue_name='datafeed',
                url='/tasks/get/fmsapi_event_alliances/' + event.key_name,
                method='GET')

        template_values = {
            'events': events
        }

        if 'X-Appengine-Taskname' not in self.request.headers:  # Only write out if not in taskqueue
            path = os.path.join(os.path.dirname(__file__), '../templates/datafeeds/usfirst_event_alliances_enqueue.html')
            self.response.out.write(template.render(path, template_values))


class FMSAPIEventAlliancesGet(webapp.RequestHandler):
    """
    Handles updating an event's alliances
    """
    def get(self, event_key):
        df = DatafeedFMSAPI('v2.0', save_response=True)

        event = Event.get_by_id(event_key)

        alliance_selections = df.getEventAlliances(event_key)

        if event and event.remap_teams:
            EventHelper.remapteams_alliances(alliance_selections, event.remap_teams)

        event_details = EventDetails(
            id=event_key,
            alliance_selections=alliance_selections
        )
        EventDetailsManipulator.createOrUpdate(event_details)

        template_values = {'alliance_selections': alliance_selections,
                           'event_name': event_details.key.id()}

        if 'X-Appengine-Taskname' not in self.request.headers:  # Only write out if not in taskqueue
            path = os.path.join(os.path.dirname(__file__), '../templates/datafeeds/usfirst_event_alliances_get.html')
            self.response.out.write(template.render(path, template_values))


class FMSAPIEventRankingsEnqueue(webapp.RequestHandler):
    """
    Handles enqueing getting rankings
    """
    def get(self, when):
        if when == "now":
            events = EventHelper.getEventsWithinADay()
            events = filter(lambda e: e.official, events)
        else:
            event_keys = Event.query(Event.official == True).filter(Event.year == int(when)).fetch(500, keys_only=True)
            events = ndb.get_multi(event_keys)

        for event in events:
            taskqueue.add(
                queue_name='datafeed',
                url='/tasks/get/fmsapi_event_rankings/' + event.key_name,
                method='GET')

        template_values = {
            'events': events,
        }

        if 'X-Appengine-Taskname' not in self.request.headers:  # Only write out if not in taskqueue
            path = os.path.join(os.path.dirname(__file__), '../templates/datafeeds/usfirst_event_rankings_enqueue.html')
            self.response.out.write(template.render(path, template_values))


class FMSAPIEventRankingsGet(webapp.RequestHandler):
    """
    Handles updating an event's rankings
    """
    def get(self, event_key):
        df = DatafeedFMSAPI('v2.0', save_response=True)

        event = Event.get_by_id(event_key)

        rankings, rankings2 = df.getEventRankings(event_key)

        if event and event.remap_teams:
            EventHelper.remapteams_rankings(rankings, event.remap_teams)
            EventHelper.remapteams_rankings2(rankings2, event.remap_teams)

        event_details = EventDetails(
            id=event_key,
            rankings=rankings,
            rankings2=rankings2
        )
        EventDetailsManipulator.createOrUpdate(event_details)

        template_values = {'rankings': rankings,
                           'event_name': event_details.key.id()}

        if 'X-Appengine-Taskname' not in self.request.headers:  # Only write out if not in taskqueue
            path = os.path.join(os.path.dirname(__file__), '../templates/datafeeds/usfirst_event_rankings_get.html')
            self.response.out.write(template.render(path, template_values))


class FMSAPIMatchesEnqueue(webapp.RequestHandler):
    """
    Handles enqueing getting match results
    """
    def get(self, when):
        if when == "now":
            events = EventHelper.getEventsWithinADay()
            events = filter(lambda e: e.official, events)
        else:
            event_keys = Event.query(Event.official == True).filter(Event.year == int(when)).fetch(500, keys_only=True)
            events = ndb.get_multi(event_keys)

        for event in events:
            taskqueue.add(
                queue_name='datafeed',
                url='/tasks/get/fmsapi_matches/' + event.key_name,
                method='GET')

        template_values = {
            'events': events,
        }

        if 'X-Appengine-Taskname' not in self.request.headers:  # Only write out if not in taskqueue
            path = os.path.join(os.path.dirname(__file__), '../templates/datafeeds/usfirst_matches_enqueue.html')
            self.response.out.write(template.render(path, template_values))


class FMSAPIMatchesGet(webapp.RequestHandler):
    """
    Handles updating matches
    """
    def get(self, event_key):
        df = DatafeedFMSAPI('v2.0', save_response=True)
        event = Event.get_by_id(event_key)

        matches = MatchHelper.delete_invalid_matches(
            df.getMatches(event_key),
            Event.get_by_id(event_key)
        )

        if event and event.remap_teams:
            EventHelper.remapteams_matches(matches, event.remap_teams)

        new_matches = MatchManipulator.createOrUpdate(matches)

        template_values = {
            'matches': new_matches,
        }

        if 'X-Appengine-Taskname' not in self.request.headers:  # Only write out if not in taskqueue
            path = os.path.join(os.path.dirname(__file__), '../templates/datafeeds/usfirst_matches_get.html')
            self.response.out.write(template.render(path, template_values))


class FMSAPITeamDetailsRollingEnqueue(webapp.RequestHandler):
    """
    Handles enqueing updates to individual teams
    Enqueues a certain fraction of teams so that all teams will get updated
    every PERIOD days.
    """
    PERIOD = 14  # a particular team will be updated every PERIOD days

    def get(self):
        now_epoch = time.mktime(datetime.datetime.now().timetuple())
        bucket_num = int((now_epoch / (60 * 60 * 24)) % self.PERIOD)

        highest_team_key = Team.query().order(-Team.team_number).fetch(1, keys_only=True)[0]
        highest_team_num = int(highest_team_key.id()[3:])
        bucket_size = int(highest_team_num / (self.PERIOD)) + 1

        min_team = bucket_num * bucket_size
        max_team = min_team + bucket_size
        team_keys = Team.query(Team.team_number >= min_team, Team.team_number < max_team).fetch(1000, keys_only=True)

        teams = ndb.get_multi(team_keys)
        for team in teams:
            taskqueue.add(
                queue_name='datafeed',
                url='/backend-tasks/get/team_details/' + team.key_name,
                method='GET')

        # FIXME omg we're just writing out? -fangeugene 2013 Nov 6
        self.response.out.write("Bucket number {} out of {}<br>".format(bucket_num, self.PERIOD))
        self.response.out.write("{} team gets have been enqueued in the interval [{}, {}).".format(len(teams), min_team, max_team))


class TeamDetailsGet(webapp.RequestHandler):
    """
    Fetches team details
    """
    def get(self, key_name):
        existing_team = Team.get_by_id(key_name)

        fms_df = DatafeedFMSAPI('v2.0')
        year = datetime.date.today().year
        fms_details = fms_df.getTeamDetails(year, key_name)

        if fms_details:
            team, district_team, robot = fms_details[0]
        else:
            team = None
            district_team = None
            robot = None

        if team:
            team = TeamManipulator.createOrUpdate(team)

        # Clean up junk district teams
        # https://www.facebook.com/groups/moardata/permalink/1310068625680096/
        dt_keys = DistrictTeam.query(
            DistrictTeam.team == existing_team.key,
            DistrictTeam.year == year).fetch(keys_only=True)
        keys_to_delete = set()
        for dt_key in dt_keys:
            if not district_team or dt_key.id() != district_team.key.id():
                keys_to_delete.add(dt_key)
        DistrictTeamManipulator.delete_keys(keys_to_delete)

        if robot:
            robot = RobotManipulator.createOrUpdate(robot)

        template_values = {
            'key_name': key_name,
            'team': team,
            'success': team is not None,
            'robot': robot,
        }

        if 'X-Appengine-Taskname' not in self.request.headers:  # Only write out if not in taskqueue
            path = os.path.join(os.path.dirname(__file__), '../templates/datafeeds/usfirst_team_details_get.html')
            self.response.out.write(template.render(path, template_values))


class TeamAvatarGet(webapp.RequestHandler):
    """
    Fetches team avatar
    """

    def get(self, key_name):
        fms_df = DatafeedFMSAPI('v2.0')
        year = datetime.date.today().year
        team = Team.get_by_id(key_name)

        avatar, keys_to_delete = fms_df.getTeamAvatar(year, key_name)

        if avatar:
            MediaManipulator.createOrUpdate(avatar)

        MediaManipulator.delete_keys(keys_to_delete)

        template_values = {
            'key_name': key_name,
            'team': team,
            'success': avatar is not None,
        }

        if 'X-Appengine-Taskname' not in self.request.headers:  # Only write out if not in taskqueue
            path = os.path.join(os.path.dirname(__file__), '../templates/datafeeds/usfirst_team_avatar_get.html')
            self.response.out.write(template.render(path, template_values))


class DistrictListGet(webapp.RequestHandler):
    """
    Fetch one year of districts only from FMS API
    """
    def get(self, year):
        df = DatafeedFMSAPI('v2.0')
        fmsapi_districts = df.getDistrictList(year)
        districts = DistrictManipulator.createOrUpdate(fmsapi_districts)

        template_values = {
            "districts": districts,
        }

        if 'X-Appengine-Taskname' not in self.request.headers:  # Only write out if not in taskqueue
            path = os.path.join(os.path.dirname(__file__), '../templates/datafeeds/fms_district_list_get.html')
            self.response.out.write(template.render(path, template_values))


class DistrictRankingsGet(webapp.RequestHandler):
    """
    Fetch district rankings from FIRST
    This data does not have full pre-event point breakdowns, but it does contain
    things like CMP advancement
    """
    def get(self, district_key):
        df = DatafeedFMSAPI('v2.0')

        district_with_rankings = df.getDistrictRankings(district_key)
        districts = []
        if district_with_rankings:
            districts = DistrictManipulator.createOrUpdate(district_with_rankings)

        template_values = {
            "districts": [districts],
        }

        if 'X-Appengine-Taskname' not in self.request.headers:  # Only write out if not in taskqueue
            path = os.path.join(os.path.dirname(__file__), '../templates/datafeeds/fms_district_list_get.html')
            self.response.out.write(template.render(path, template_values))


class TbaVideosEnqueue(webapp.RequestHandler):
    """
    Handles enqueing grabing tba_videos for Matches at individual Events.
    """
    def get(self):
        events = Event.query()

        for event in events:
            taskqueue.add(
                url='/tasks/get/tba_videos/' + event.key_name,
                method='GET')

        template_values = {
            'event_count': Event.query().count(),
        }

        if 'X-Appengine-Taskname' not in self.request.headers:  # Only write out if not in taskqueue
            path = os.path.join(os.path.dirname(__file__), '../templates/datafeeds/tba_videos_enqueue.html')
            self.response.out.write(template.render(path, template_values))


class TbaVideosGet(webapp.RequestHandler):
    """
    Handles reading a TBA video listing page and updating the match objects in the datastore as needed.
    """
    def get(self, event_key):
        df = DatafeedTba()

        event = Event.get_by_id(event_key)
        match_filetypes = df.getVideos(event)
        if match_filetypes:
            matches_to_put = []
            for match in event.matches:
                if match.tba_videos != match_filetypes.get(match.key_name, []):
                    match.tba_videos = match_filetypes.get(match.key_name, [])
                    match.dirty = True
                    matches_to_put.append(match)

            MatchManipulator.createOrUpdate(matches_to_put)

            tbavideos = match_filetypes.items()
        else:
            logging.info("No tbavideos found for event " + event.key_name)
            tbavideos = []

        template_values = {
            'tbavideos': tbavideos,
        }

        if 'X-Appengine-Taskname' not in self.request.headers:  # Only write out if not in taskqueue
            path = os.path.join(os.path.dirname(__file__), '../templates/datafeeds/tba_videos_get.html')
            self.response.out.write(template.render(path, template_values))


class HallOfFameTeamsGet(webapp.RequestHandler):
    """
    Handles scraping the list of Hall of Fame teams from FIRST resource library.
    """
    def get(self):
        df = DatafeedResourceLibrary()

        teams = df.getHallOfFameTeams()
        if teams:
            media_to_update = []
            for team in teams:
                team_reference = Media.create_reference('team', team['team_id'])

                video_foreign_key = team['video']
                if video_foreign_key:
                    media_to_update.append(Media(id=Media.render_key_name(MediaType.YOUTUBE_VIDEO, video_foreign_key),
                                                 media_type_enum=MediaType.YOUTUBE_VIDEO,
                                                 media_tag_enum=[MediaTag.CHAIRMANS_VIDEO],
                                                 references=[team_reference],
                                                 year=team['year'],
                                                 foreign_key=video_foreign_key))

                presentation_foreign_key = team['presentation']
                if presentation_foreign_key:
                    media_to_update.append(Media(id=Media.render_key_name(MediaType.YOUTUBE_VIDEO, presentation_foreign_key),
                                                 media_type_enum=MediaType.YOUTUBE_VIDEO,
                                                 media_tag_enum=[MediaTag.CHAIRMANS_PRESENTATION],
                                                 references=[team_reference],
                                                 year=team['year'],
                                                 foreign_key=presentation_foreign_key))

                essay_foreign_key = team['essay']
                if essay_foreign_key:
                    media_to_update.append(Media(id=Media.render_key_name(MediaType.EXTERNAL_LINK, essay_foreign_key),
                                                 media_type_enum=MediaType.EXTERNAL_LINK,
                                                 media_tag_enum=[MediaTag.CHAIRMANS_ESSAY],
                                                 references=[team_reference],
                                                 year=team['year'],
                                                 foreign_key=essay_foreign_key))

            MediaManipulator.createOrUpdate(media_to_update)
        else:
            logging.info("No Hall of Fame teams found")
            teams = []

        template_values = {
            'teams': teams,
        }

        if 'X-Appengine-Taskname' not in self.request.headers:  # Only write out if not in taskqueue
            path = os.path.join(os.path.dirname(__file__), '../templates/datafeeds/hall_of_fame_teams_get.html')
            self.response.out.write(template.render(path, template_values))


class TeamBlacklistWebsiteDo(webapp.RequestHandler):
    """
    Blacklist the current website for a team
    """
    def get(self, key_name):
        team = Team.get_by_id(key_name)

        if team.website:
            WebsiteBlacklist.blacklist(team.website)

        self.redirect('/backend-tasks/get/team_details/{}'.format(key_name))
