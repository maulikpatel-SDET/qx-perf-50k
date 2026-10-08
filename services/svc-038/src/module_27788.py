"""Service module 27788: business logic, no crypto."""


def calculate_total_27788(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27788():
    return 'module 27788 handles orders and invoices'
