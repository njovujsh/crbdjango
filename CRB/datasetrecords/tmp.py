current_ref = split_ret_last_or_first(reference_number, get_ref_only=True)
            p_type = split_ret_last_or_first(reference_number, last_=False)
            num_times = split_ret_last_or_first(reference_number, last_=True)
            
            if(p_type.strip().lstrip().rstrip() == product_type.strip().lstrip().rstrip()):
                print "They are Equal..."
                inc = increment_index(int(num_times))
                new_ref_by = current_ref + ":" + str(product_type) + ":" + str(inc)
                return new_ref_by
            else:
                print "QUERYING ", reference_number, "PRODUCT TYPE ", ptype
                query_ref = query_reference_numbers(reference_number)
                if(query_ref):
                    product_type = product_representation(ptype)
                    
                    current_ref = split_ret_last_or_first(query_ref.account_reference, get_ref_only=True)
                    p_type = split_ret_last_or_first(query_ref.account_reference, last_=False)
                    num_times = split_ret_last_or_first(query_ref.account_reference, last_=True)

                    print "p_type ", p_type, "PRODUCT TYPE ", product_type
                    if(p_type.strip().lstrip().rstrip() == product_type.strip().lstrip().rstrip()):
                        inc = increment_index(int(num_times))
                        new_ref_by = current_ref + ":" + str(product_type) + ":" + str(inc)
                        return new_ref_by
                    else:
                        index = reference_number.index(":")
                        product_type = product_representation(ptype)
                        
                        newreference = reference_number[:index] + ":" + product_type + str(1)
                        return newreference
                 
                else:  
                    if(numtimes):
                        index = reference_number.index(":")
                        product_type = product_representation(ptype)
                        
                        newreference = reference_number[:index] + ":" + product_type + str(1)
                        return newreference
                    else:
                        index = reference_number.index(":")
                        product_type = product_representation(ptype)
                        
                        newreference = reference_number[:index] + ":" + product_type
                        return newreference
