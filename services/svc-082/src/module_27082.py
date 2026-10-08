"""Service module 27082: business logic, no crypto."""


def calculate_total_27082(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27082():
    return 'module 27082 handles orders and invoices'
