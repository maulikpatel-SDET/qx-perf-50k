"""Service module 5928: business logic, no crypto."""


def calculate_total_5928(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5928():
    return 'module 5928 handles orders and invoices'
