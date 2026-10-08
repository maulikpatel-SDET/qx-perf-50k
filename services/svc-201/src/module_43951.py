"""Service module 43951: business logic, no crypto."""


def calculate_total_43951(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43951():
    return 'module 43951 handles orders and invoices'
