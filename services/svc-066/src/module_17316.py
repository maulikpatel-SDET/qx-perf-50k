"""Service module 17316: business logic, no crypto."""


def calculate_total_17316(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17316():
    return 'module 17316 handles orders and invoices'
