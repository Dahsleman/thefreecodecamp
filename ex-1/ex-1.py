def arithmetic_arranger(my_list,b = False):
    op_list = ["*", "/"]
    add_list = ["+"]
    problems = 0
    letters = 0
    numbers = 0
    op_1 = 0
        # codigo dos erros
    for item in my_list:
            op = any(s in op_list for s in item)
            problems = problems+1
            for i in item:
                if op == True:
                    op_1 += 1
                    break
                if i.isalpha() == True:
                    letters = 1
                    break
                else:
                    add_1 = item.split()
                    num_1 = len(add_1[0])
                    num_2 = len(add_1[2])
                    if num_1 > 4:
                        numbers = 1
                        break
                    elif num_2 > 4:
                        numbers = 1
                        break
            if letters == 1:
                return("Error: Numbers must only contain digits.")
            elif numbers == 1:
                return("Error: Numbers cannot be more than four digits.")
            elif problems > 5:
                return("Error: Too many problems.")
            elif op_1 != 0:
                return("Error: Operator must be '+' or '-'.")
            elif problems <= 5:
            # codigo do print das funcoes
                numerator_list = list()
                denominador_list = list()
                result_list = list()
                tracinho_list = list()
                formula_1 = ''
                for item in my_list:
                    add = any(s in item for s in add_list)
                    if add == True:
                        add_1 = item.split()
                        if len(add_1[0]) >= len(add_1[2]):
                            n = len(add_1[0]) + 2
                            n1 = len(add_1[0]) + 1
                            numerator = '{:>{width}}'.format(add_1[0], width=n)
                            numerator_list.append(numerator)
                            denominador_2 = '{:>{width}}'.format(add_1[2], width=n1)
                            denominador = '+'
                            denominador += denominador_2
                            denominador_list.append(denominador)
                            r = int(add_1[0]) + int(add_1[2])
                            result = '{:>{width}}'.format(r, width=n)
                            result_list.append(result)
                            n_tracinho = 0
                            tracinho = ''
                            while n_tracinho < n:
                                tracinho += '-'  
                                n_tracinho +=1
                            else:
                                tracinho_list.append(tracinho)
                        elif len(add_1[0]) < len(add_1[2]):
                            n = len(add_1[2]) + 2
                            n1 = len(add_1[2]) + 1
                            numerator = '{:>{width}}'.format(add_1[0], width=n)
                            numerator_list.append(numerator)
                            denominador_2 = '{:>{width}}'.format(add_1[2], width=n1)
                            denominador = '+'
                            denominador += denominador_2
                            denominador_list.append(denominador)
                            r = int(add_1[0]) + int(add_1[2])
                            result = '{:>{width}}'.format(r, width=n)
                            result_list.append(result)
                            n_tracinho = 0
                            tracinho = ''
                            while n_tracinho < n:
                                tracinho += '-'  
                                n_tracinho +=1
                            else:
                                tracinho_list.append(tracinho)
                    else:
                        add_1 = item.split()
                        if len(add_1[0]) >= len(add_1[2]):
                            n = len(add_1[0]) + 2
                            n1 = len(add_1[0]) + 1
                            numerator = '{:>{width}}'.format(add_1[0], width=n)
                            numerator_list.append(numerator)
                            denominador_2 = '{:>{width}}'.format(add_1[2], width=n1)
                            denominador = '-'
                            denominador += denominador_2
                            denominador_list.append(denominador)
                            r = int(add_1[0]) - int(add_1[2])
                            result = '{:>{width}}'.format(r, width=n)
                            result_list.append(result)
                            n_tracinho = 0
                            tracinho = ''
                            while n_tracinho < n:
                                tracinho += '-'  
                                n_tracinho +=1
                            else:
                                tracinho_list.append(tracinho)
                        elif len(add_1[0]) < len(add_1[2]):
                            n = len(add_1[2]) + 2
                            n1 = len(add_1[2]) + 1
                            numerator = '{:>{width}}'.format(add_1[0], width=n)
                            numerator_list.append(numerator)
                            denominador_2 = '{:>{width}}'.format(add_1[2], width=n1)
                            denominador = '-'
                            denominador += denominador_2
                            denominador_list.append(denominador)
                            r = int(add_1[0]) - int(add_1[2])
                            result = '{:>{width}}'.format(r, width=n)
                            result_list.append(result)
                            n_tracinho = 0
                            tracinho = ''
                            while n_tracinho < n:
                                tracinho += '-'  
                                n_tracinho +=1
                            else:
                                tracinho_list.append(tracinho)
    if b == True:
            x = "    ".join(numerator_list)
            d = "    ".join(denominador_list)
            t = "    ".join(tracinho_list)
            u = "    ".join(result_list)
            return("{}\n{}\n{}\n{}".format(x,d,t,u))           
    else:
            x = "    ".join(numerator_list)
            d = "    ".join(denominador_list)
            t = "    ".join(tracinho_list)
            return("{}\n{}\n{}".format(x,d,t))  
x = arithmetic_arranger(['3 + 1','55 + 2','8 - 1000','1 + 1','2 + 2'],True)
print(x)