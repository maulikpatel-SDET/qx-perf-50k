"""Service module 34835: business logic, no crypto."""


def calculate_total_34835(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34835():
    return 'module 34835 handles orders and invoices'
