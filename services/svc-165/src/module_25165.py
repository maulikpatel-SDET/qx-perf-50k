"""Service module 25165: business logic, no crypto."""


def calculate_total_25165(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25165():
    return 'module 25165 handles orders and invoices'
