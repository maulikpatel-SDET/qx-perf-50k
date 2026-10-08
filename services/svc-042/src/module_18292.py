"""Service module 18292: business logic, no crypto."""


def calculate_total_18292(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18292():
    return 'module 18292 handles orders and invoices'
