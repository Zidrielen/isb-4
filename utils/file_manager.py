import json
import logging
import sys

logging.getLogger().setLevel(logging.INFO)


class FileManager:
    """Class for working with program files"""

    def __init__(self, json_file: str = "files/settings.json") -> None:
        """
        Constructor

        :param json_file - Path to .json file
        """
        settings = self.read_settings(json_file)
        self.__hash_file_path = settings["hash_file"]
        self.__last_numbers_file_path = settings["last_numbers_file"]
        self.__bins_file_path = settings["bins_file"]
        self.__card_number_file_path = settings["card_number_file"]
        self.__statistic_file_path = settings["statistic_file"]

    def read_settings(self, settings_file) -> dict:
        """
        Method reads the settings file

        :param file_name - name of the settings file
        :return - dictionary of paths to program files
        """
        try:
            with open(settings_file) as json_file:
                settings = json.load(json_file)
            logging.info(
                f"Settings file successfully loaded from {settings_file}")
        except OSError as err:
            logging.warning(
                f"Settings file wasn't loaded from {settings_file}")
            sys.exit(err)
        return settings
    
