user_categories = {}

with open('purchase_log.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            data = eval(line)
            user_id = data['user_id']
            category = data['category']
            user_categories[user_id] = category

print(f"Найдено {len(user_categories)} пользователей с покупками")

with open('visit_log__1_.csv', 'r', encoding='utf-8') as visits, \
        open('funnel.csv', 'w', encoding='utf-8') as funnel:
    funnel.write('user.id,source,category\n')
    header = next(visits)

    processed = 0
    written = 0

    for line in visits:
        parts = line.strip().split(',')
        if len(parts) >= 2:
            user_id, source = parts[0], parts[1]

            if user_id in user_categories:
                category = user_categories[user_id]
                funnel.write(f'{user_id},{source},{category}\n')
                written += 1

            processed += 1

            if processed % 10000 == 0:
                print(f'Обработано {processed} строк, найдено {written} покупок')

print(f"Готово! Обработано {processed} строк, записано {written} покупок")

print("\nПервые 3 строки funnel.csv:")
with open('funnel.csv', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i < 4:
            print(line.strip())
        else:
            break