from typing import Dict, Set

from backend.common.models.keys import Year

"""
Valid breakdowns are those used for seeding. Varies by year.
For 2014, seeding outlined in Section 5.3.4 in the 2014 manual.
For 2016+, valid breakdowns match those provided by the FRC API.
"""
VALID_BREAKDOWNS: Dict[Year, Set[str]] = {
    2014: set(["auto", "assist", "truss+catch", "teleop_goal+foul"]),
    2015: set(
        [
            "coopertition_points",
            "auto_points",
            "container_points",
            "tote_points",
            "litter_points",
            "foul_points",
        ]
    ),
    2016: set(
        [
            "adjustPoints",
            "autoBoulderPoints",
            "autoBouldersHigh",
            "autoBouldersLow",
            "autoCrossingPoints",
            "autoPoints",
            "autoReachPoints",
            "breachPoints",
            "capturePoints",
            "foulCount",
            "foulPoints",
            "position1crossings",
            "position2",
            "position2crossings",
            "position3",
            "position3crossings",
            "position4",
            "position4crossings",
            "position5",
            "position5crossings",
            "robot1Auto",
            "robot2Auto",
            "robot3Auto",
            "techFoulCount",
            "teleopBoulderPoints",
            "teleopBouldersHigh",
            "teleopBouldersLow",
            "teleopChallengePoints",
            "teleopCrossingPoints",
            "teleopDefensesBreached",
            "teleopPoints",
            "teleopScalePoints",
            "teleopTowerCaptured",
            "totalPoints",
            "towerEndStrength",
            "towerFaceA",
            "towerFaceB",
            "towerFaceC",
        ]
    ),
    2017: set(
        [
            "adjustPoints",
            "autoFuelHigh",
            "autoFuelLow",
            "autoFuelPoints",
            "autoMobilityPoints",
            "autoPoints",
            "autoRotorPoints",
            "foulCount",
            "foulPoints",
            "kPaBonusPoints",
            "kPaRankingPointAchieved",
            "robot1Auto",
            "robot2Auto",
            "robot3Auto",
            "rotor1Auto",
            "rotor1Engaged",
            "rotor2Auto",
            "rotor2Engaged",
            "rotor3Engaged",
            "rotor4Engaged",
            "rotorBonusPoints",
            "rotorRankingPointAchieved",
            "techFoulCount",
            "teleopFuelHigh",
            "teleopFuelLow",
            "teleopFuelPoints",
            "teleopPoints",
            "teleopRotorPoints",
            "teleopTakeoffPoints",
            "totalPoints",
            "touchpadFar",
            "touchpadMiddle",
            "touchpadNear",
        ]
    ),
    2018: set(
        [
            "autoRobot1",
            "autoRobot2",
            "autoRobot3",
            "autoSwitchOwnershipSec",
            "autoScaleOwnershipSec",
            "autoSwitchAtZero",
            "autoRunPoints",
            "autoOwnershipPoints",
            "autoPoints",
            "teleopSwitchOwnershipSec",
            "teleopScaleOwnershipSec",
            "teleopSwitchBoostSec",
            "teleopScaleBoostSec",
            "teleopSwitchForceSec",
            "teleopScaleForceSec",
            "vaultForceTotal",
            "vaultForcePlayed",
            "vaultLevitateTotal",
            "vaultLevitatePlayed",
            "vaultBoostTotal",
            "vaultBoostPlayed",
            "endgameRobot1",
            "endgameRobot2",
            "endgameRobot3",
            "teleopOwnershipPoints",
            "vaultPoints",
            "endgamePoints",
            "teleopPoints",
            "autoQuestRankingPoint",
            "faceTheBossRankingPoint",
            "foulCount",
            "techFoulCount",
            "adjustPoints",
            "foulPoints",
            "rp",
            "totalPoints",
            # fields added by TBA:
            "tba_gameData",
        ]
    ),
    2019: set(
        [
            "adjustPoints",
            "autoPoints",
            "bay1",
            "bay2",
            "bay3",
            "bay4",
            "bay5",
            "bay6",
            "bay7",
            "bay8",
            "cargoPoints",
            "completeRocketRankingPoint",
            "completedRocketFar",
            "completedRocketNear",
            "endgameRobot1",
            "endgameRobot2",
            "endgameRobot3",
            "foulCount",
            "foulPoints",
            "habClimbPoints",
            "habDockingRankingPoint",
            "habLineRobot1",
            "habLineRobot2",
            "habLineRobot3",
            "hatchPanelPoints",
            "lowLeftRocketFar",
            "lowLeftRocketNear",
            "lowRightRocketFar",
            "lowRightRocketNear",
            "midLeftRocketFar",
            "midLeftRocketNear",
            "midRightRocketFar",
            "midRightRocketNear",
            "preMatchBay1",
            "preMatchBay2",
            "preMatchBay3",
            "preMatchBay6",
            "preMatchBay7",
            "preMatchBay8",
            "preMatchLevelRobot1",
            "preMatchLevelRobot2",
            "preMatchLevelRobot3",
            "rp",
            "sandStormBonusPoints",
            "techFoulCount",
            "teleopPoints",
            "topLeftRocketFar",
            "topLeftRocketNear",
            "topRightRocketFar",
            "topRightRocketNear",
            "totalPoints",
        ]
    ),
    2020: set(
        [
            "adjustPoints",
            "autoCellPoints",
            "autoCellsBottom",
            "autoCellsInner",
            "autoCellsOuter",
            "autoInitLinePoints",
            "autoPoints",
            "controlPanelPoints",
            "endgamePoints",
            "endgameRobot1",
            "endgameRobot2",
            "endgameRobot3",
            "endgameRungIsLevel",
            "foulCount",
            "foulPoints",
            "initLineRobot1",
            "initLineRobot2",
            "initLineRobot3",
            "rp",
            "shieldEnergizedRankingPoint",
            "shieldOperationalRankingPoint",
            "stage1Activated",
            "stage2Activated",
            "stage3Activated",
            "stage3TargetColor",
            "techFoulCount",
            "teleopCellPoints",
            "teleopCellsBottom",
            "teleopCellsInner",
            "teleopCellsOuter",
            "teleopPoints",
            "totalPoints",
        ]
    ),
    2021: set(
        [
            "adjustPoints",
            "autoCellPoints",
            "autoCellsBottom",
            "autoCellsInner",
            "autoCellsOuter",
            "autoInitLinePoints",
            "autoPoints",
            "controlPanelPoints",
            "endgamePoints",
            "endgameRobot1",
            "endgameRobot2",
            "endgameRobot3",
            "endgameRungIsLevel",
            "foulCount",
            "foulPoints",
            "initLineRobot1",
            "initLineRobot2",
            "initLineRobot3",
            "rp",
            "shieldEnergizedRankingPoint",
            "shieldOperationalRankingPoint",
            "stage1Activated",
            "stage2Activated",
            "stage3Activated",
            "stage3TargetColor",
            "techFoulCount",
            "teleopCellPoints",
            "teleopCellsBottom",
            "teleopCellsInner",
            "teleopCellsOuter",
            "teleopPoints",
            "totalPoints",
        ]
    ),
    2022: set(
        [
            "adjustPoints",
            "autoCargoLowerBlue",
            "autoCargoLowerFar",
            "autoCargoLowerNear",
            "autoCargoLowerRed",
            "autoCargoPoints",
            "autoCargoTotal",
            "autoCargoUpperBlue",
            "autoCargoUpperFar",
            "autoCargoUpperNear",
            "autoCargoUpperRed",
            "autoPoints",
            "autoTaxiPoints",
            "cargoBonusRankingPoint",
            "endgamePoints",
            "endgameRobot1",
            "endgameRobot2",
            "endgameRobot3",
            "foulCount",
            "foulPoints",
            "hangarBonusRankingPoint",
            "matchCargoTotal",
            "quintetAchieved",
            "rp",
            "taxiRobot1",
            "taxiRobot2",
            "taxiRobot3",
            "techFoulCount",
            "teleopCargoLowerBlue",
            "teleopCargoLowerFar",
            "teleopCargoLowerNear",
            "teleopCargoLowerRed",
            "teleopCargoPoints",
            "teleopCargoTotal",
            "teleopCargoUpperBlue",
            "teleopCargoUpperFar",
            "teleopCargoUpperNear",
            "teleopCargoUpperRed",
            "teleopPoints",
            "totalPoints",
        ]
    ),
    2023: set(
        [
            "activationBonusAchieved",
            "adjustPoints",
            "autoBridgeState",
            "autoChargeStationPoints",
            "autoChargeStationRobot1",
            "autoChargeStationRobot2",
            "autoChargeStationRobot3",
            "autoCommunity",
            "autoDocked",
            "autoGamePieceCount",
            "autoGamePiecePoints",
            "autoMobilityPoints",
            "autoPoints",
            "coopertitionCriteriaMet",
            "coopGamePieceCount",
            "endGameBridgeState",
            "endGameChargeStationPoints",
            "endGameChargeStationRobot1",
            "endGameChargeStationRobot2",
            "endGameChargeStationRobot3",
            "endGameParkPoints",
            "extraGamePieceCount",
            "foulCount",
            "foulPoints",
            "g405Penalty",
            "h111Penalty",
            "linkPoints",
            "links",
            "mobilityRobot1",
            "mobilityRobot2",
            "mobilityRobot3",
            "rp",
            "sustainabilityBonusAchieved",
            "techFoulCount",
            "teleopCommunity",
            "teleopGamePieceCount",
            "teleopGamePiecePoints",
            "teleopPoints",
            "totalChargeStationPoints",
            "totalPoints",
            # fields added by TBA:
            "tba_extraRp1",
            "tba_extraRp2",
        ]
    ),
    2024: set(
        [
            "adjustPoints",
            "autoAmpNoteCount",
            "autoAmpNotePoints",
            "autoLeavePoints",
            "autoLineRobot1",
            "autoLineRobot2",
            "autoLineRobot3",
            "autoPoints",
            "autoSpeakerNoteCount",
            "autoSpeakerNotePoints",
            "autoTotalNotePoints",
            "coopertitionBonusAchieved",
            "coopertitionCriteriaMet",
            "coopNotePlayed",
            "endGameHarmonyPoints",
            "endGameNoteInTrapPoints",
            "endGameOnStagePoints",
            "endGameParkPoints",
            "endGameRobot1",
            "endGameRobot2",
            "endGameRobot3",
            "endGameSpotLightBonusPoints",
            "endGameTotalStagePoints",
            "ensembleBonusAchieved",
            "ensembleBonusOnStageRobotsThreshold",
            "ensembleBonusStagePointsThreshold",
            "foulCount",
            "foulPoints",
            "g206Penalty",
            "g408Penalty",
            "g424Penalty",
            "melodyBonusAchieved",
            "melodyBonusThreshold",
            "melodyBonusThresholdCoop",
            "melodyBonusThresholdNonCoop",
            "micCenterStage",
            "micStageLeft",
            "micStageRight",
            "rp",
            "techFoulCount",
            "teleopAmpNoteCount",
            "teleopAmpNotePoints",
            "teleopPoints",
            "teleopSpeakerNoteAmplifiedCount",
            "teleopSpeakerNoteAmplifiedPoints",
            "teleopSpeakerNoteCount",
            "teleopSpeakerNotePoints",
            "teleopTotalNotePoints",
            "totalPoints",
            "trapCenterStage",
            "trapStageLeft",
            "trapStageRight",
            # fields added by TBA:
            "tba_extraRp1",
            "tba_extraRp2",
        ]
    ),
    # when adding new fields, please keep them sorted alphabetically
}


class ScoreBreakdownKeys:
    @staticmethod
    def get_valid_score_breakdown_keys(year: Year) -> set[str]:
        """
        Return all valid score breakdown keys for the given year.
        """
        # return a copy
        return set(VALID_BREAKDOWNS.get(year, set()))
