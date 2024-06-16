#%%
import lightkurve as lk 
from astropy import units as u
from astropy.time import Time
from astropy.timeseries import TimeSeries
import matplotlib.pyplot as plt
import matplotlib_inline

search = lk.search_lightcurve('Pi Mensae', mission = 'TESS', author = 'SPOC')
lc = search[0].download()
lc.select_flux('pdcsap_flux')
lc = lc.flatten(window_length = 501).remove_outliers()
flux_values =lc.flux.value
time_values = lc.time.value

#change BTJD values into typical 3d value
time_btjd = Time(time_values, format = 'btjd', scale = 'tdb')
time_jd = time_btjd.jd
print('time values in 3d:', time_jd)
plt.scatter(time_jd, flux_values)

from astropy.stats import LombScargle
time_values = np.array(time_values)
flux_values = np.arrau