function words(str) {
    var cleanStr = str.replace(/[\s\t\n]+/g,' ');
    var the_words = cleanStr.split(" ");
    var dictionary = Object.create(null);
    for (var index = 0; index < the_words.length; index++) {
        var word = the_words[index];
        if (!dictionary[word]) {
            dictionary[word] = 1;
        } else {
            dictionary[word]++;
        }
    }
    return dictionary
}