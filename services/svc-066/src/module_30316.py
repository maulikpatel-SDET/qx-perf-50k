"""Service module 30316: business logic, no crypto."""


def calculate_total_30316(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30316():
    return 'module 30316 handles orders and invoices'
