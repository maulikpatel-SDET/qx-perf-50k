"""Service module 41814: business logic, no crypto."""


def calculate_total_41814(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41814():
    return 'module 41814 handles orders and invoices'
