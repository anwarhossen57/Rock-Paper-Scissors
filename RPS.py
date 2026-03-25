def player(prev_play, history=[], patterns={}):
    # ১. নতুন গেম শুরু হলে রিসেট
    if not prev_play:
        history.clear()
        patterns.clear()
        prev_play = 'R'

    history.append(prev_play)
    counter_move = {'R': 'P', 'P': 'S', 'S': 'R'}
    
    # ২. ডিফল্ট চাল হিসেবে 'R' রাখা (যাতে KeyError না আসে)
    best_prediction = "R" 

    # ৩. শুরুতে ডাটা কম থাকলে মোস্ট ফ্রিকোয়েন্ট চাল প্রেডিক্ট করা
    if len(history) < 10:
        most_frequent = max(set(history), key=history.count)
        return counter_move[most_frequent]

    # ৪. মাল্টি-লেভেল প্যাটার্ন অ্যানালাইসিস
    max_confidence = -1
    for length in range(3, 7):
        if len(history) < length + 1:
            continue
        
        past_ctx = "".join(history[-(length + 1) : -1])
        current_move = history[-1]
        
        key = f"{length}x{past_ctx}"
        if key not in patterns:
            patterns[key] = {'R': 0, 'P': 0, 'S': 0}
        patterns[key][current_move] += 1

        current_ctx = "".join(history[-length:])
        lookup = f"{length}x{current_ctx}"

        if lookup in patterns:
            stats = patterns[lookup]
            total_seen = sum(stats.values())
            if total_seen > 0:
                predicted = max(stats, key=stats.get)
                confidence = stats[predicted] / total_seen
                if confidence > max_confidence:
                    max_confidence = confidence
                    best_prediction = predicted

    # ৫. নিশ্চিত করা যে আমরা সবসময় R, P, বা S রিটার্ন করছি
    return counter_move.get(best_prediction, 'R')