// Generate all combinations of strings with specified maximum
// lenght and set of characters to use

function gen_strings(str_length, charset) {
    charset = charset.split('');
    strings = charset

    for ( let i = 1; i < str_length; i++ ) {
        let temp = [];
        for ( let k = 0; k < strings.length; k++ ) {
            string = strings[k];
            if (i === 1) {
                temp.push(string);
            }
            for ( let m = 0; m < charset.length; m++ ) {
                let letter = charset[m];
                temp.push(string + letter);
            }
        }
        strings = temp;
    }
    return strings;
}