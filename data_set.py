def load_data_set():
    post_list = [
        "my dog has flea problems help please",
        "my dalmation is so cute I love him my",
        "mr licks ate my steak how to stop him",
        "maybe not take him to dog park stupid",
        "stop posting stupid worthless garbage",
        "quit buying worthless dog food stupid"
    ]
    class_list = ["normal", "normal", "normal", "abusive", "abusive", "abusive"]
    test_list = [
        "my dog has flea problems help please",
        "stop posting stupid worthless garbage"
    ]
    return post_list, class_list, test_list
