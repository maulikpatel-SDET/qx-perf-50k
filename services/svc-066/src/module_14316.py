"""Service module 14316: business logic, no crypto."""


def calculate_total_14316(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14316():
    return 'module 14316 handles orders and invoices'
