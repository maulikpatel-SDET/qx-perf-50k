"""Service module 6719: business logic, no crypto."""


def calculate_total_6719(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6719():
    return 'module 6719 handles orders and invoices'
