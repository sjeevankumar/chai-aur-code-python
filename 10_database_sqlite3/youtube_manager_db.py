import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute(''' 
               CREATE TABLE IF NOT EXISTS videos(
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   time TEXT NOT NULL
               )
        ''')

def list_videos():
    cursor.execute('SELECT * FROM videos')
    for row in cursor.fetchall():
        print(row)

def add_video():
    name = input('Enter the video name: ')
    time = input('Enter the video time: ')
    
    cursor.execute('INSERT INTO videos(name,time) VALUES (?,?)',(name,time))
    conn.commit()

def update_video():
    video_id = input('Enter video ID to update: ')
    new_name = input('Enter the video name: ')
    new_time = input('Enter the video time: ')
    
    cursor.execute('UPDATE videos SET name = ?,time = ? WHERE id = ?',(new_name,new_time,video_id))
    conn.commit()

def delete_video():
    video_id = input('Enter video ID to delete: ')
    
    cursor.execute('DELETE FROM videos WHERE id=?',(video_id,))
    conn.commit()

def main():
    while True:
        print('\n Youtube manager app with DB')
        print('1. List Videos')
        print('2. Add Videos')
        print('3. Update Videos')
        print('4. Delete Videos')
        print('5. Exit App')
        
        choice = input('Enter your choice: ')
        if choice == '1':
            list_videos()
        elif choice == '2':
            add_video()
        elif choice == '3':
            update_video()  
        elif choice == '4':
            delete_video()
        elif choice == '5':
            break
        else:
            print('invalid choice')          
    
    conn.close()  

if __name__ == '__main__':
    main()


