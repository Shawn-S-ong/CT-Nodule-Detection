config = {'datapath':'C:\\Users\\s4548361\\Desktop\\DSB2017-master\\work\\test',
          'preprocess_result_path':'C:\\Users\\s4548361\\Desktop\\DSB2017-master\\work\\test',
          'outputfile':'prediction.csv',
          
          'detector_model':'net_detector',
         # 'detector_param':'./model/detector.ckpt',
          'detector_param':'./model/170.ckpt',
         'classifier_model':'net_classifier',
         'classifier_param':'./model/classifier.ckpt',
         'n_gpu':8,
         'n_worker_preprocessing':None,
         'use_exsiting_preprocessing':False,
         'skip_preprocessing':True,
         'skip_detect':False}
