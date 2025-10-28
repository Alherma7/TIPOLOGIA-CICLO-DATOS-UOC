# config

DRIVER_NAME = "msedgedriver.exe"
BASE_URL = "https://www.allrecipes.com/"
SELECTORS = {
    "cookies": "onetrust-accept-btn-handler",
    "menu": "#header_1-0 > div.mntl-header__menu-top > div.mntl-header__menu-button-container > button",
    "cuisines": "//*[@id='mntl-fullscreen-nav_1-0']/ul/li[5]/a",
    "view_all": "//*[@id='mntl-fullscreen-nav__sublist-cuisines-mntl-fullscreen-nav']/ul/li[9]/a",
    "cuisines_list":"a.mntl-link-list__link"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

