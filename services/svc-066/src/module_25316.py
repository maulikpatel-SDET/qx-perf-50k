"""Service module 25316: business logic, no crypto."""


def calculate_total_25316(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25316():
    return 'module 25316 handles orders and invoices'
