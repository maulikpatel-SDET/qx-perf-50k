"""Service module 44951: business logic, no crypto."""


def calculate_total_44951(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44951():
    return 'module 44951 handles orders and invoices'
