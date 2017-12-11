import ElansaryM_inc , ElansaryM_init , ElansaryM_fun


for output_name_ , output_ in zip (ElansaryM_init.outputs_names_,ElansaryM_init.outputs_):
    print '='*80
    print("%s : %s" % ("Analysis and Predictions for",output_name_))
    print '='*80

    X , y = ElansaryM_init.dataset.iloc[:,4:28] , ElansaryM_init.dataset.iloc[:, output_]

    #splits the data so some can be used for testing 50%
    X_train, X_test, y_train, y_test = ElansaryM_inc.train_test_split(X, y, test_size= .5, random_state=44)

    for classifier_name, classifier_ in zip(ElansaryM_init.classifiers_names, ElansaryM_init.classifiers_):
        ElansaryM_fun.ME_Predictions (classifier_name,classifier_, X_train, y_train, X_test, y_test)



# 1 Well Name
# 2 Easting
# 3 Northing
# 4 MD
# 5 TVD
# 6 Azimuth
# 7 Inclination
# 8 Deviation-DownDip
# 9 Deviation-UpDip
# 10 Deviation-NoDip
# 11 Porosity%
# 12 Gross Thickness(ft)
# 13 NTG
# 14 Sw(%)
# 15 TOC %
# 16 Comp-Perforated Lateral (ft)
# 17 Comp-Stimulated Lateral Length (ft)
# 18 Comp-Clusters per Stage
# 19 Comp-Shot Density (shots-ft)
# 20 Comp-Avg Stage Length(ft)
# 21 Comp-Number of Stages
# 22 Stim-Avg. Tr. Pressure (psi)
# 23 Stim-Avg. Tr. Rate (bbl-min)
# 24 Stim-Fluid volume per Stage (bbl)
# 25 Stim-clean volume per Stage (bbl)
# 26 Stim-Slurry volume per Stage (bbl)
# 27 Stim-Maximum propant Conc-(lb-gal)
# 28 Stim-Proppant per stage(lb)
# 29 30 Day Cum Gas (MCF)
# 30 30 Day Cum Condensate (bbls)
# 31 90 Day Cum Gas (MCF)
# 32 90 Day Cum Condensate (bbls)
# 33 120 Day Cum Gas (MCF)
# 34 120 Day Cum Condensate (bbls)
# 35 180 Day -Cum Gas (MCF)
# 36 180 Day -Cum Condensate (bbls)
