#%%
import lightkurve as lk 
import matplotlib_inline

tpf_example = lk.search_tesscut('Polaris')
download = tpf_example[6].download()

#%%
custom_mask = download.create_threshold_mask(threshold = 0.5)
download.plot(aperture_mask = custom_mask)
lc = download.to_lightcurve(aperture_mask = custom_mask)
lc.plot()

