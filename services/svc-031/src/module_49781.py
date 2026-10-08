"""Service module 49781: business logic, no crypto."""


def calculate_total_49781(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49781():
    return 'module 49781 handles orders and invoices'
