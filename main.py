from synology_api import filestation
import sys
# Initiate the classes DownloadStation & FileStation with (ip_address, port, username, password)
# it will log in automatically 
# NOTE: for Filestation and Downloadstation only has been added interactive_output=True,
# It can be omitted and initiate the wrapper with the below ove code

print(sys.argv[1])

# domain: hklab one
fl = filestation.FileStation('external_domain', '6491', 'username', 'password', secure=True, cert_verify=True, dsm_version=7, debug=False, otp_code=sys.argv[1])

# print(fl.get_list_share())

# arr = ['khan', 'pathan']

# # for a in arr:
# fl.create_folder('/demo', 'khan')
# path = "/demo/pathan"
# fl.upload_file(path,'./HK Administration setup.pdf')
# print(fl.create_sharing_link('/demo/pathan/', 'apple123@biomed',))


# dwn = downloadstation.DownloadStation('Synology Ip', 'Synology Port', 'Username', 'Password', secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None)

# dwn.get_info()

path = '/Clinic/Reports/BioMed/qPCR'
reponse = fl.get_list_share()

print(reponse)


