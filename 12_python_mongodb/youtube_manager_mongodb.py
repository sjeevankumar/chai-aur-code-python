from pymongo import MongoClient
from bson import ObjectId

# Not a good idea to include id and password in code files
try:
    client = MongoClient('mongodb+srv://username:password@cluster0.uossfjm.mongodb.net/ytmanager')
    print('connection to db established successfully')
except Exception as e:
    print('error while establishing connection to db')
    exit()

db = client['ytmanager']
video_collection = db['videos']

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name:{video['name']} and Time: {video['time']}")

def add_video():
    name = input('Enter the video name: ')
    time = input('Enter the video time: ')
    
    video_collection.insert_one({'name':name,'time':time})

def update_video():
    video_id = input('Enter the video id to update: ')
    new_name = input('Enter the updated video name: ')
    new_time = input('Enter the updated video time: ')
    
    video_collection.update_one(
        {'_id':ObjectId(video_id)},
        {'$set':{'name':new_name,'time':new_time}}
    )

def delete_video():
    video_id = input('Enter the video id to be delete: ')
    
    video_collection.delete_one({'_id':ObjectId(video_id)})

def main():
    while True:
        print('\n Youtube manager app')
        print('1. List all videos')
        print('2. Add a new video')
        print('3. Update a video')
        print('4. Delete a video')
        print('5. Exit the app')
        
        choice = input('Enter your choice: ')
        match choice:
            case '1':
                list_videos()
            case '2':
                add_video()
            case '3':
                update_video()
            case '4':
                delete_video()
            case '5':
                break
            case _:
                print('invalid choice')

if __name__ == '__main__':
    main()


