{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "import datetime\n",
    "import time\n",
    "import keyboard"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Current google-chrome version is 86.0.4240\n",
      "[WDM] - Get LATEST driver version for 86.0.4240\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " \n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Driver [/home/asharib/.wdm/drivers/chromedriver/linux64/86.0.4240.22/chromedriver] found in cache\n"
     ]
    },
    {
     "ename": "ImportError",
     "evalue": "You must be root to use this library on linux.",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mImportError\u001b[0m                               Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-80-88c514d2555e>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     13\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     14\u001b[0m \u001b[0mobj\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mzoom_bot\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 15\u001b[0;31m \u001b[0mobj\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mjoin\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlink\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m<ipython-input-80-88c514d2555e>\u001b[0m in \u001b[0;36mjoin\u001b[0;34m(self, meeting_link)\u001b[0m\n\u001b[1;32m      4\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbot\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmeeting_link\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m         \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m         \u001b[0mkeyboard\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"tab\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdo_press\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdo_release\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      7\u001b[0m         \u001b[0mkeyboard\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"enter\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdo_press\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdo_release\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m         \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m10\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.8/site-packages/keyboard/__init__.py\u001b[0m in \u001b[0;36msend\u001b[0;34m(hotkey, do_press, do_release)\u001b[0m\n\u001b[1;32m    377\u001b[0m     \u001b[0m_listener\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mis_replaying\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    378\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 379\u001b[0;31m     \u001b[0mparsed\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mparse_hotkey\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mhotkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    380\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mstep\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mparsed\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    381\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mdo_press\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.8/site-packages/keyboard/__init__.py\u001b[0m in \u001b[0;36mparse_hotkey\u001b[0;34m(hotkey)\u001b[0m\n\u001b[1;32m    356\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mstep\u001b[0m \u001b[0;32min\u001b[0m \u001b[0m_re\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mr',\\s?'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mhotkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    357\u001b[0m         \u001b[0mkeys\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_re\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mr'\\s?\\+\\s?'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstep\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 358\u001b[0;31m         \u001b[0msteps\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtuple\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey_to_scan_codes\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mkey\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mkeys\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    359\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mtuple\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msteps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    360\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.8/site-packages/keyboard/__init__.py\u001b[0m in \u001b[0;36m<genexpr>\u001b[0;34m(.0)\u001b[0m\n\u001b[1;32m    356\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mstep\u001b[0m \u001b[0;32min\u001b[0m \u001b[0m_re\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mr',\\s?'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mhotkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    357\u001b[0m         \u001b[0mkeys\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_re\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mr'\\s?\\+\\s?'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstep\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 358\u001b[0;31m         \u001b[0msteps\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtuple\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey_to_scan_codes\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mkey\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mkeys\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    359\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mtuple\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msteps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    360\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.8/site-packages/keyboard/__init__.py\u001b[0m in \u001b[0;36mkey_to_scan_codes\u001b[0;34m(key, error_if_missing)\u001b[0m\n\u001b[1;32m    315\u001b[0m     \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    316\u001b[0m         \u001b[0;31m# Put items in ordered dict to remove duplicates.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 317\u001b[0;31m         \u001b[0mt\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mtuple\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0m_collections\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mOrderedDict\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mscan_code\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mscan_code\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmodifier\u001b[0m \u001b[0;32min\u001b[0m \u001b[0m_os_keyboard\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmap_name\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnormalized\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    318\u001b[0m         \u001b[0me\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    319\u001b[0m     \u001b[0;32mexcept\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mKeyError\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mexception\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.8/site-packages/keyboard/__init__.py\u001b[0m in \u001b[0;36m<genexpr>\u001b[0;34m(.0)\u001b[0m\n\u001b[1;32m    315\u001b[0m     \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    316\u001b[0m         \u001b[0;31m# Put items in ordered dict to remove duplicates.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 317\u001b[0;31m         \u001b[0mt\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mtuple\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0m_collections\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mOrderedDict\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mscan_code\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mscan_code\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmodifier\u001b[0m \u001b[0;32min\u001b[0m \u001b[0m_os_keyboard\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmap_name\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnormalized\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    318\u001b[0m         \u001b[0me\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    319\u001b[0m     \u001b[0;32mexcept\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mKeyError\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mexception\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.8/site-packages/keyboard/_nixkeyboard.py\u001b[0m in \u001b[0;36mmap_name\u001b[0;34m(name)\u001b[0m\n\u001b[1;32m    146\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    147\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mmap_name\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 148\u001b[0;31m     \u001b[0mbuild_tables\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    149\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mentry\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mfrom_name\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    150\u001b[0m         \u001b[0;32myield\u001b[0m \u001b[0mentry\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.8/site-packages/keyboard/_nixkeyboard.py\u001b[0m in \u001b[0;36mbuild_tables\u001b[0;34m()\u001b[0m\n\u001b[1;32m     62\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mbuild_tables\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     63\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mto_name\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mfrom_name\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;32mreturn\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 64\u001b[0;31m     \u001b[0mensure_root\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     65\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     66\u001b[0m     modifiers_bits = {\n",
      "\u001b[0;32m~/anaconda3/lib/python3.8/site-packages/keyboard/_nixcommon.py\u001b[0m in \u001b[0;36mensure_root\u001b[0;34m()\u001b[0m\n\u001b[1;32m    172\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mensure_root\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    173\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mos\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgeteuid\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 174\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mImportError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'You must be root to use this library on linux.'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mImportError\u001b[0m: You must be root to use this library on linux."
     ]
    }
   ],
   "source": [
    "class zoom_bot:\n",
    "    def join(self,meeting_link):\n",
    "        self.bot = webdriver.Chrome(ChromeDriverManager().install())\n",
    "        self.bot.get(meeting_link)\n",
    "        time.sleep(3)\n",
    "        keyboard.send(\"tab\", do_press=True, do_release=True)\n",
    "        keyboard.send(\"enter\", do_press=True, do_release=True)\n",
    "        time.sleep(10)\n",
    "\n",
    "        self.bot.quit()\n",
    "\n",
    "link = open(\"meeting_link.txt\",\"r\").read()\n",
    "\n",
    "obj = zoom_bot()\n",
    "obj.join(link)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
