"""Service module 36449: business logic, no crypto."""


def calculate_total_36449(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36449():
    return 'module 36449 handles orders and invoices'
