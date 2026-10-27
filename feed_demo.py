"""Build a feed for a community you choose.

See the course lab page for the demonstration checklist.
"""

from lab_classes import User, Tweet


def build_feed():
    jayla = User('jayla')
    teammate = User('teammate')

    users = [jayla, teammate]

    post1 = Tweet('jayla', 'Ready for our next tournament! #Golf')
    post2 = Tweet('teammate', 'Working on my putting today. #Practice')
    post3 = Tweet('jayla', 'Made a birdie on the last hole! #Golf')

    posts = [post1, post2, post3]

    # jayla gains two followers, then loses one
    jayla.follow()
    jayla.follow()
    jayla.unfollow()

    # teammate gets a follower too
    teammate.follow()

    # a post gets two likes, then someone takes one back
    post1.like()
    post1.like()
    post1.unlike()

    post3.like()

    return users, posts


def main():
    users, posts = build_feed()

    print('Golf team accounts:')
    for user in users:
        print(user)

    print('Golf team posts:')
    for post in posts:
        print(post)
        print(post.hashtags())


if __name__ == '__main__':
    main()
