"""Service module 44835: business logic, no crypto."""


def calculate_total_44835(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44835():
    return 'module 44835 handles orders and invoices'
