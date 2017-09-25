<b>European Astro-Pi challenge 2016-2017</b> <br>
<b>Team name:</b> GKGF-1 - Gymnasium of Kanithos (Chalkida) Greece <br>
<b>Reference about challenge:</b> <br>
<ul>
<li> <a href="https://astro-pi.org/past-missions" target="_blank"> </a> <br>
<li> http://www.esa.int/Education/AstroPI/European_Astro_Pi_Challenge_Code_your_ISS_experiment_-_more_details2 <br>
<li> http://www.esa.int/Education/AstroPI/1st_European_Astro_Pi_Challenge_Timeline <br>
<li> http://www.esa.int/Education/AstroPI/Meet_the_sense_hat_-_teach_with_space_T05.2http://www.esa.int/Education/AstroPI/Meet_the_sense_hat_-_teach_with_space_T05.2 <br>
<li> http://www.esa.int/Education/AstroPI/Getting_started_with_Astro_Pi_-_teach_with_space_T05.1 <br>
<li> http://www.esa.int/Education/AstroPI/How_to_collect_data_from_the_Astro_Pi_-_teach_with_space_T05.3 <br>
<li> http://www.esa.int/Education/AstroPI/Phase_2_of_the_European_Astro_Pi_challenge_begins <br>
<li> http://www.esa.int/Education/Teachers_Corner/European_Astro_Pi_Challenge_Phase_2_update <br>
<li> http://www.esa.int/Education/AstroPI/2016_-_2017_European_Astro_Pi_Challenge_winners_announced <br>
<li> http://www.esa.int/Education/AstroPI/2016_17_European_Astro_Pi_Challenge_Winners <br>
</ul>
<b>Our missions: </b> <br>
<ul>
<li> <i>Primary: </i> <br>
<ul>
<li> Receiving measurements from all SenseHAT sensors per 10secs (temperature from humidity,
temperature from pressure, relative humidity, pressure, orientation (in radians and degrees),
accelerometer (raw and degrees), compass (direction of North and raw), gyroscope (raw and
degrees) and CPU temperature at Raspberry PI3 model B). <br>
<li> Timestamp for each measurement (in format: dd/mm/yyyy and hh:mm:ss). <br>
<li> Monitoring living conditions of the ISS crew per 10 sec. Living conditions on ISS are: temperature
(min 18.3 o C – max 26.6 o C), relative humidity (min 50% - max 70%), pressure (min 979.0559 mbar –
max 1027.2769 mbar). Displaying of notifying messages on the 8x8 led display of SenseHAT if the
measurements of the sensors (temperature, humidity, pressure) are above or below the allowed
limit. <br>
<li> For monitoring temperature we use the average measurement of temperature from the humidity
sensor and temperature from the pressure sensor. <br>
<li> All our programme is conducted in 3 hours (10800 sec). <br>
<li> If there is a slight variation of temperature/humidity in the original measurements which will be
received after commencing the programme (approximately 60 sec) we assume that somebody will
be in proximity to Astro-Pi and a greeting message (Hi!) will be displayed in the 8x8 led display. <br>
</ul>
<li> <i>Secondary: </i> <br>
<ul>
<li> From Newton's Second Law and gravitational force it is evident that ISS speed is given by the
formula u=sqrt(G*m/R), where: G=6,67428×10^−11 (Nm^2/kg^2) - Gravitational constant,
m=5.972*10^24 Kg - mass of Earth, R=(Radius of Earth + altitude of ISS). <br>
<li> In calculating the Earth radius we take into consideration ISS latitude. <br>
<li> We use http://celestrak.com/NORAD/elements/stations.txt (NORAD Two-Line Element Sets) - we
would appreciate it if you notified the 2 lines from NORAD TLE at the beginning of our programme
BEFORE putting it into practice (lines 23 & 24 in our python code with name GKGF_1.py). <br>
<li> Calculation centripetal and centripetal acceleration (mass of ISS=419455 Kg). <br>
<li> Calculating rotation period of ISS around the Earth. <br>
<li> Storing of timestamp, latitude (in decimal format), longitude (in decimal format) and altitude of
ISS (in meters) in separate file from the one with the sensor measurements. <br>
</ul>
</ul>
<b>Reference about our missions:</b> <br>
<ul>
<li> www.celestrak.com/NORAD/elements/stations.txt <br>
<li> http://wsn.spaceflight.esa.int/docs/Factsheets/30%20ECLSS%20LR.pdf <br>
<li> http://pep8online.com <br>
<li> http://pypi.python.org/pypi/pep8 <br>
<li> www.faa.gov/about/office_org/headquarters_offices/avs/offices/aam/cami/library/online_libraries/aerospace_medicine/tutorial/media/iii.1.2_cabin_environment_and_eva_environment.doc<br>
<li> www.weather.gov/media/epz/wxcalc/tempConvert.pdf <br>
<li> UNIVERSITY PHYSICS WITH MODERN PHYSICS - 13<sup>TH</sup> EDITION - HUGH D. YOUNG - ROGER A. FREEDMAN <br>
<li> Physics (Student Book) from Greek Public High School-ISBN 978-960-06-4827-0 (in Greek language)
</ul>
<b>Files description: </b> <br>
<ul>
<li> GKGF_1.py - the Python programm running on ISS <br>
<li> GKGF-1_GKGF_1_Greece_20170501_115603.csv - Data from ISS (from 01/05/2017,11:56:03 until 01/05/2017,14:55:51) - All mesurments from all sensors of SenseHat <br>
<li> GKGF-1_GKGF_1_Greece_calc_20170501_115603.csv - Data from ISS (from 01/05/2017,11:56:03 until 01/05/2017,14:55:51) - Position of ISS (latitude , longitude , altitude) <br>
</ul>
<b>Many thanks to: </b> <br>
<ul>
<li> My students (Paraskevas, Nikos, Pavlos, Constantinos and Anastasia) <br>
<li> Mr Tsamouris Tasos - Physics Teacher at 4<sup>th</sup> Lyceum of Chalkida for his scientific support <br>
<li> Mrs Pappa Korina - English Teacher at Gymnasium of Kanithos her translating assistance from Greek to English. <br>
</ul>
  
