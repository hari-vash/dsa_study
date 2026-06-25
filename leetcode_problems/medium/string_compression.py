class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        -----GIVEN EXAMPLE-----
        Input: chars = ["a","a","b","b","c","c","c"]
        Output: 6
        -----------------------
        write = 0
        read = 0
        
        while read<len(chars):
            while 0<7
                current_char = char[read]                                   => current_char = char[0]       => current_char = 'a'
                count = 0
                while read<len(chars) and chars[read] == current_char:
                    while 0<7 and chars[0] == current_char:                 => true and true
                        read += 1                                           => read = 1
                        count += 1                                          => count = 1
                    while 1<7 and chars[1] == current_char:                 => true and true
                        read += 1                                           => read = 2
                        count += 1                                          => count = 2
                    while 2<7 and chars[1] == current_char:                 => true and false

                chars[write] = current_char                                 => chars[0] = 'a'               => chars = ["a","a","b","b","c","c","c"]
                write += 1                                                  => write = 1
                if count > 1:                                               => true
                    for digit in str(count):                                => digit = '2'
                        chars[write] = 2                                    => chars[1]                     => chars = ["a","2","b","b","c","c","c"]
                        write += 1                                          => write = 2
                        
            while 2<7
                current_char = char[read]                                   => current_char = char[2]       => current_char = 'b'
                count = 0
                while read<len(chars) and chars[read] == current_char:
                    while 2<7 and chars[2] == current_char:                 => true and true
                        read += 1                                           => read = 3
                        count += 1                                          => count = 1
                    while 3<7 and chars[3] == current_char:                 => true and true
                        read += 1                                           => read = 4
                        count += 1                                          => count = 2
                    while 4<7 and chars[4] == current_char:                 => true and false

                chars[write] = current_char                                 => chars[2] = 'b'               => chars = ["a","2","b","b","c","c","c"]
                write += 1                                                  => write = 3
                if count > 1:                                               => true
                    for digit in str(count):                                => digit = '2'
                        chars[write] = 3                                    => chars[3]                     => chars = ["a","2","b","2","c","c","c"]
                        write += 1                                          => write = 4
            
            while 4<7
                current_char = char[read]                                   => current_char = char[4]       => current_char = 'c'
                count = 0
                while read<len(chars) and chars[read] == current_char:
                    while 4<7 and chars[4] == current_char:                 => true and true
                        read += 1                                           => read = 5
                        count += 1                                          => count = 1
                    while 5<7 and chars[5] == current_char:                 => true and true
                        read += 1                                           => read = 6
                        count += 1                                          => count = 2
                    while 6<7 and chars[6] == current_char:                 => true and true
                        read += 1                                           => read = 7
                        count += 1                                          => count = 3
                    while 7<7 and chars[7] == current_char:                 => false and false

                chars[write] = current_char                                 => chars[4] = 'c'               => chars = ["a","2","b","2","c","c","c"]
                write += 1                                                  => write = 5
                if count > 1:                                               => true
                    for digit in str(count):                                => digit = '3'
                        chars[write] = 3                                    => chars[5]                     => chars = ["a","2","b","2","c","3","c"]
                        write += 1                                          => write = 6
                        
            while 7<7:                                                      => false
            
        return write                                                        => return 6                     => solution
        """
        write = 0
        read = 0

        while read<len(chars):
            current_char = chars[read]
            count = 0

            while read<len(chars) and chars[read] == current_char:
                read+=1
                count+=1
            
            chars[write] = current_char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            
        return write