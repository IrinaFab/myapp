# myapp
This app was deployed via a CI/CD pipeline and hosted on Google Cloud Platform. The app produces 14 days forecast of number of COVID-19 cases in Romania. For my application, I used Johns Hopkins COVID-19 confirmed cases dataset available in BigQuery.

The first six entries on April 2, 2020.


<img width="158" alt="Screen Shot 2022-06-04 at 3 00 38 PM" src="https://user-images.githubusercontent.com/90358148/172023813-94e99df0-c6ff-4026-830c-d74c460d6b82.png">

The last six entries on June 6, 2022.


<img width="158" alt="Screen Shot 2022-06-04 at 3 00 38 PM" src="https://user-images.githubusercontent.com/90358148/172023955-dbe4e535-f8ab-47fe-84b5-0a860db8008c.png">



The graph of number of reports produced with Data Studio.

![Screen Shot 2022-06-04 at 3 07 37 PM](https://user-images.githubusercontent.com/90358148/172023999-3ee4d625-5ca2-4a22-bf61-995a08dc46c2.png)


1.	New repo myapp
2.	New project in GCP
o	Enable billing for the Cloud project
o	Enable Cloud Build API 
3.	If first time, create ssh key ssh-keygen -t rsa
4.	Run the "cat" command with the public file
5.	Create new ssh key in GitHub
6.	git clone
7.	Change to the directory that contains the sample code
8.	Create and source the virtual environment
virtualenv python3 -m venv ~/.myapp
source ~/.gcp-getting-started/bin/activate. (save it: vim ~/.bashrc)


The model was produced using the following code:


![Screen Shot 2022-06-04 at 3 08 31 PM](https://user-images.githubusercontent.com/90358148/172024037-1f63255d-ab9a-4193-9f1f-74698c2dca61.png)





The time series model


![Screen Shot 2022-06-04 at 3 08 37 PM](https://user-images.githubusercontent.com/90358148/172024044-fd821c46-3993-4477-a7d9-28676bf6e31c.png)



The app result


![Screen Shot 2022-06-04 at 3 08 45 PM](https://user-images.githubusercontent.com/90358148/172024113-673c597d-823c-46f8-9540-6903ccc06c4f.png)



