
const notCon = document.getElementById('notCon')





function get_flashed_messages() {
    fetch('/get-flashed-messages', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'with-categories': true
        }
    })
    .then(response => {return response.json()})
    .then(data => {
        for (var notification of data) {
            console.log(notification);
            if (notification.category) {
                createNotification(notification.message, notification.category);
            } else {
                createNotification(notification.message);
            }
        }
    })
    .catch(error => console.error('NotificationError:', error));
}

get_flashed_messages();