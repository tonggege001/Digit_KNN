//
// Created by tonggege on 17-10-27.
//
#include <opencv2/opencv.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/ml/ml.hpp>

#define exp 220

using namespace cv;
using namespace std;
//处理图片
int loaddata(float label[exp*10][10],float set[exp*10][900]){
    //设置标签
    for(int i = 0;i<exp*10;i++){
        for(int j = 0;j<10;j++){
            label[i][j] = 0;
        }
    }
    for(int i = 0;i<exp*10;i++){
        switch(i/exp){
            case 0:label[i][0] = 1;break;
            case 1:label[i][1] = 1;break;
            case 2:label[i][2] = 1;break;
            case 3:label[i][3] = 1;break;
            case 4:label[i][4] = 1;break;
            case 5:label[i][5] = 1;break;
            case 6:label[i][6] = 1;break;
            case 7:label[i][7] = 1;break;
            case 8:label[i][8] = 1;break;
            case 9:label[i][9] = 1;break;
        }
    }
    //设置训练集
    for(int i = 0;i<10;i++){
        for(int j = 1;j<=exp;j++){
            string filepath = "trainSet/";
            filepath.append(to_string(i));
            filepath.append("/");
            filepath.append(to_string(j));
            filepath.append(".jpg");
            Mat image = imread(filepath,CV_LOAD_IMAGE_GRAYSCALE);
    //        cout << image << endl;
            int a = 0;
            for(int k = 0;k<image.rows;k++){
                for(int z = 0;z<image.cols;z++){
                    set[exp*i+j-1][a++] = image.at<char>(k,z);
                }
            }
        }
    }
}

int trainBody(){

    CvANN_MLP ann;//声明神经网络

    CvANN_MLP_TrainParams params;//声明神经网络参数
    params.train_method = CvANN_MLP_TrainParams::BACKPROP;  //反向传播
    params.bp_dw_scale = 0.1;   //学习率
    params.bp_moment_scale = 0.1;

    float labels[exp*10][10];
    float trainingData[exp*10][900];
    loaddata(labels,trainingData);
    Mat labelsMat(exp*10, 10, CV_32FC1, labels);
    Mat trainingDataMat(exp*10, 900, CV_32FC1, trainingData);
    Mat layerSizes = (Mat_<int>(1, 3) << 900,50,10);
    ann.create(layerSizes, CvANN_MLP::SIGMOID_SYM);//CvANN_MLP::SIGMOID_SYM
    //CvANN_MLP::GAUSSIAN
    //CvANN_MLP::IDENTITY
    ann.train(trainingDataMat, labelsMat, Mat(), Mat(), params);
    ann.save("annData.xml");
}

int main789(){
    CvANN_MLP ann;//声明神经网络
    //trainBody();
    ann.load("annData.xml");
    for(int k = 1;k<=10;k++){
        string path = "testSet/6/";
        path.append(to_string(k)+".jpg");
        Mat samples = imread(path,CV_LOAD_IMAGE_GRAYSCALE);
        Mat sample = (Mat_<float>(1,900));
        int a = 0;
        for(int i = 0;i<samples.rows;i++){
            for(int j = 0;j<samples.cols;j++){
                sample.at<float>(0,a++) = (float)(samples.at<char>(i,j));
            }
        }
        Mat sampleLabel;
        ann.predict(sample, sampleLabel);
        cout << sampleLabel << endl;
        float *pp = sampleLabel.ptr<float>(0);
        int max = 0;
        for(int i = 0;i<10;i++){
            if(pp[i]>pp[max]) max = i;
        }
        cout << max <<endl;

    }

    return 0;
}





















