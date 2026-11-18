from analysis.base_analysis import BaseAnalysis
from analysis_factory import AnalysisFactory
from Dream_Book_Shop import DEFAULT_DATASET_FILE, MENU_OPTIONS, clean_file_name


def test_factory_creates_analysis_objects_for_menu_choices():
    for choice in ["1", "2", "3", "4", "5", "6"]:
        analysis = AnalysisFactory.create_analysis(choice)
        assert isinstance(analysis, BaseAnalysis)


def test_factory_returns_none_for_invalid_choice():
    analysis = AnalysisFactory.create_analysis("9")

    assert analysis is None


def test_cli_menu_has_expected_options():
    assert list(MENU_OPTIONS.keys()) == ["1", "2", "3", "4", "5", "6", "7", "8"]
    assert MENU_OPTIONS["7"] == "Show all graphs"
    assert MENU_OPTIONS["8"] == "Exit"


def test_cli_uses_default_dataset_file():
    assert DEFAULT_DATASET_FILE == "books.csv"


def test_cli_cleans_file_name_input():
    assert clean_file_name(' "books.csv" ') == "books.csv"
    assert clean_file_name("\ufeffbooks.csv") == "books.csv"
    assert clean_file_name(chr(239) + chr(187) + chr(191) + "books.csv") == "books.csv"
