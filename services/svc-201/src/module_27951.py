"""Service module 27951: business logic, no crypto."""


def calculate_total_27951(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27951():
    return 'module 27951 handles orders and invoices'
