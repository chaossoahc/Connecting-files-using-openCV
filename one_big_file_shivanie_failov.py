import cv2
import numpy as np
import os 

path_list = os.listdir("F:/create_all_diap/40_41/")

for pacient in path_list:


    # pacient = "sub-47_task-motor-imagery_eeg.edf"
    output_filename = 'F:/'+pacient+'.avi'
    frame_width = 640*8
    frame_height = 480*5
    fps = 25  # Частота кадров
    codec = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_filename, codec, fps, (frame_width, frame_height))
    # pacient = "sub-50_task-motor-imagery_eeg.edf"

    video_freq1  = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/1_2output_video.avi"
    video_freq2  = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/2_3output_video.avi"
    video_freq3  = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/3_4output_video.avi"
    video_freq4  = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/4_5output_video.avi"
    video_freq5  = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/5_6output_video.avi"
    video_freq6  = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/6_7output_video.avi"
    video_freq7  = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/7_8output_video.avi"
    video_freq8  = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/8_9output_video.avi"
    video_freq9  = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/9_10output_video.avi"
    video_freq10 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/10_11output_video.avi"
    video_freq11 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/11_12output_video.avi"
    video_freq12 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/12_13output_video.avi"
    video_freq13 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/13_14output_video.avi"
    video_freq14 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/14_15output_video.avi"
    video_freq15 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/15_16output_video.avi"
    video_freq16 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/16_17output_video.avi"
    video_freq17 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/17_18output_video.avi"
    video_freq18 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/18_19output_video.avi"
    video_freq19 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/19_20output_video.avi"
    video_freq20 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/20_21output_video.avi"
    video_freq21 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/21_22output_video.avi"
    video_freq22 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/22_23output_video.avi"
    video_freq23 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/23_24output_video.avi"
    video_freq24 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/24_25output_video.avi"
    video_freq25 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/25_26output_video.avi"
    video_freq26 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/26_27output_video.avi"
    video_freq27 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/27_28output_video.avi"
    video_freq28 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/28_29output_video.avi"
    video_freq29 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/29_30output_video.avi"
    video_freq30 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/30_31output_video.avi"
    video_freq31 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/31_32output_video.avi"
    video_freq32 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/32_33output_video.avi"
    video_freq33 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/33_34output_video.avi"
    video_freq34 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/34_35output_video.avi"
    video_freq35 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/35_36output_video.avi"
    video_freq36 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/36_37output_video.avi"
    video_freq37 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/37_38output_video.avi"
    video_freq38 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/38_39output_video.avi"
    video_freq39 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/39_40output_video.avi"
    video_freq40 = "J:/insult_data_LAZURENKO/create_all_diap/"+pacient+"/40_41output_video.avi"


    cap1  = cv2.VideoCapture(video_freq1)
    cap2  = cv2.VideoCapture(video_freq2)
    cap3  = cv2.VideoCapture(video_freq3)
    cap4  = cv2.VideoCapture(video_freq4)
    cap5  = cv2.VideoCapture(video_freq5)
    cap6  = cv2.VideoCapture(video_freq6)
    cap7  = cv2.VideoCapture(video_freq7)
    cap8  = cv2.VideoCapture(video_freq8)
    cap9  = cv2.VideoCapture(video_freq9)
    cap10 = cv2.VideoCapture(video_freq10)
    cap11 = cv2.VideoCapture(video_freq11)
    cap12 = cv2.VideoCapture(video_freq12)
    cap13 = cv2.VideoCapture(video_freq13)
    cap14 = cv2.VideoCapture(video_freq14)
    cap15 = cv2.VideoCapture(video_freq15)
    cap16 = cv2.VideoCapture(video_freq16)
    cap17 = cv2.VideoCapture(video_freq17)
    cap18 = cv2.VideoCapture(video_freq18)
    cap19 = cv2.VideoCapture(video_freq19)
    cap20 = cv2.VideoCapture(video_freq20)
    cap21 = cv2.VideoCapture(video_freq21)
    cap22 = cv2.VideoCapture(video_freq22)
    cap23 = cv2.VideoCapture(video_freq23)
    cap24 = cv2.VideoCapture(video_freq24)
    cap25 = cv2.VideoCapture(video_freq25)
    cap26 = cv2.VideoCapture(video_freq26)
    cap27 = cv2.VideoCapture(video_freq27)
    cap28 = cv2.VideoCapture(video_freq28)
    cap29 = cv2.VideoCapture(video_freq29)
    cap30 = cv2.VideoCapture(video_freq30)
    cap31 = cv2.VideoCapture(video_freq31)
    cap32 = cv2.VideoCapture(video_freq32)
    cap33 = cv2.VideoCapture(video_freq33)
    cap34 = cv2.VideoCapture(video_freq34)
    cap35 = cv2.VideoCapture(video_freq35)
    cap36 = cv2.VideoCapture(video_freq36)
    cap37 = cv2.VideoCapture(video_freq37)
    cap38 = cv2.VideoCapture(video_freq38)
    cap39 = cv2.VideoCapture(video_freq39)
    cap40 = cv2.VideoCapture(video_freq40)

    duration = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
    for frame in range(duration):
        print(frame/duration*100, )
        ret1, frame1  = cap1.read() 
        ret2, frame2  = cap2.read() 
        ret3, frame3  = cap3.read() 
        ret4, frame4  = cap4.read() 
        ret5, frame5  = cap5.read() 
        ret6, frame6  = cap6.read() 
        ret7, frame7  = cap7.read() 
        ret8, frame8  = cap8.read() 
        ret9, frame9  = cap9.read() 
        ret10, frame10 = cap10.read() 
        ret11, frame11 = cap11.read() 
        ret12, frame12 = cap12.read() 
        ret13, frame13 = cap13.read() 
        ret14, frame14 = cap14.read() 
        ret15, frame15 = cap15.read() 
        ret16, frame16 = cap16.read() 
        ret17, frame17 = cap17.read() 
        ret18, frame18 = cap18.read() 
        ret19, frame19 = cap19.read() 
        ret20, frame20 = cap20.read() 
        ret21, frame21 = cap21.read() 
        ret22, frame22 = cap22.read() 
        ret23, frame23 = cap23.read() 
        ret24, frame24 = cap24.read() 
        ret25, frame25 = cap25.read() 
        ret26, frame26 = cap26.read() 
        ret27, frame27 = cap27.read() 
        ret28, frame28 = cap28.read() 
        ret29, frame29 = cap29.read() 
        ret30, frame30 = cap30.read() 
        ret31, frame31 = cap31.read() 
        ret32, frame32 = cap32.read() 
        ret33, frame33 = cap33.read() 
        ret34, frame34 = cap34.read() 
        ret35, frame35 = cap35.read() 
        ret36, frame36 = cap36.read() 
        ret37, frame37 = cap37.read() 
        ret38, frame38 = cap38.read() 
        ret39, frame39 = cap39.read() 
        ret40, frame40 = cap40.read()
        combined_image_horizontal1 = np.hstack((frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8))
        combined_image_horizontal2 = np.hstack((frame9, frame10, frame11, frame12, frame13, frame14, frame15, frame16))
        combined_image_horizontal3 = np.hstack((frame17, frame18, frame19, frame20, frame21, frame22, frame23, frame24)) 
        combined_image_horizontal4 = np.hstack((frame25, frame26, frame27, frame28, frame29, frame30, frame31, frame32))
        combined_image_horizontal5 = np.hstack((frame33, frame34, frame35, frame36, frame37, frame38, frame39, frame40))
        combined_image_all = np.vstack((combined_image_horizontal1, combined_image_horizontal2, combined_image_horizontal3, combined_image_horizontal4, combined_image_horizontal5))
        # frame_width = combined_image_all.shape[1]
        # frame_height = combined_image_all.shape[0]

        framess = cv2.resize(combined_image_all, (frame_width, frame_height))
        # cv2.imwrite('F:/test/combined_image_horizontal'+str(frame)+'.png', combined_image_all)
        # Запись кадра в видео
        out.write(framess)

    out.release()
    cv2.destroyAllWindows()

    print('Video saved successfully.')






















