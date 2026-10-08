"""Service module 18316: business logic, no crypto."""


def calculate_total_18316(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18316():
    return 'module 18316 handles orders and invoices'
