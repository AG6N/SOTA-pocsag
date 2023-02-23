# SOTA-pocsag
A simple python program used to send SOTA spots from an inexpensive Pi-star / MMDVM system without using Dapnet Rubrics.  This script polls the SOTA API every 90 seconds and grabs the ID of the spot.  If the spot ID is different, it sends the callsign, frequency, mode and summit info to a pager, then loops to check for any updates.

Tested with Pi-Star V4.1.6, a cheap MMDVM/ Rasberry Pi, and a Alphapoc 602R style pager.  Any pager from the following list should work too.
https://hampager.de/dokuwiki/doku.php?id=pager_comparison
