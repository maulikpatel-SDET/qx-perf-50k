"""Service module 38719: business logic, no crypto."""


def calculate_total_38719(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38719():
    return 'module 38719 handles orders and invoices'
