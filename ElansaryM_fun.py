import ElansaryM_init

def ME_print(v1,v2):
    print ("\t%s,%s" % ( v2 ,v1 ))
    # print ("%s :\t%f" % ( v1 ,v2 ))

def ME_Predictions(classifier_name , classifier , xtrn , ytrn , xtst , ytst):
    classifier.fit(xtrn, ytrn)
    predictions = classifier.predict(xtst)
    print '-'*80
    print("%s: %s" % ("Classifier" , classifier_name) )
    print '-'*80
    print '-'*25
    print("%s" % ("Regression metrics") )
    print '-'*25
    for reg_metric_name_, reg_metric_ in zip(ElansaryM_init.reg_metrics_names_,ElansaryM_init.reg_metrics_):
        ME_print(reg_metric_name_, reg_metric_(ytst,predictions))
    print("%s" % ("Classification metrics") )
    print '-'*25
    for cls_metric_name_, cls_metric_ in zip(ElansaryM_init.cls_metrics_names_,ElansaryM_init.cls_metrics_):
        ME_print(cls_metric_name_, cls_metric_(ytst,predictions))
