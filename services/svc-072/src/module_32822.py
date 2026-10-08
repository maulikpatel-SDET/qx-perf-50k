"""Service module 32822: business logic, no crypto."""


def calculate_total_32822(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32822():
    return 'module 32822 handles orders and invoices'
