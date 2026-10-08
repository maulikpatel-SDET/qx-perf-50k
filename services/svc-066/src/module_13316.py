"""Service module 13316: business logic, no crypto."""


def calculate_total_13316(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13316():
    return 'module 13316 handles orders and invoices'
