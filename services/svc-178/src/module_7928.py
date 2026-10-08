"""Service module 7928: business logic, no crypto."""


def calculate_total_7928(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7928():
    return 'module 7928 handles orders and invoices'
