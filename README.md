# SOTA-pocsag

Two simple python programs used to send Summits On The Air spots to inexpensive alphanumeric pagers using either a Pi-Star/MMDVM or Unipager, without subscribing to Dapnet Rubrics.  It works by polling the SOTA API every 60 seconds and grabs the ID of the spot.  If the spot ID is different, it sends the callsign, frequency, mode and summit info to a pager on RIC 56, then loops to check for any updates.

SOTA-pocsag-MMDM.py was tested with Pi-Star V4.1.6, a cheap MMDVM/ Rasberry Pi.  You will need to apt-get a Python environment
to your Pi-Star.

SOTA-pocsag-unipager tested on Debian 11, with software available here --> https://github.com/rwth-afu/UniPager
Obvously, this needs some kind of transmitter, as is intended for wide area paging.  When SOTA spots are sent to
Unipager, transmit timeslots are observed.  This is not the case with MMDVM.

Learn more about Dapnet here --> https://github.com/rwth-afu/UniPager

I tested with an Alphapoc 602R style pager.  Any pager from the following list should work too, as long as you can modify the RIC numbers
https://hampager.de/dokuwiki/doku.php?id=pager_comparison
