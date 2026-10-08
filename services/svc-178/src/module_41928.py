"""Service module 41928: business logic, no crypto."""


def calculate_total_41928(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41928():
    return 'module 41928 handles orders and invoices'
